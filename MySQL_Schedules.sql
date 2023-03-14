
SHOW EVENTS;
--mysql -u root -p

DROP EVENT UpdateMatches;

SELECT @@event_scheduler;
SET GLOBAL event_scheduler = ON;
  
  -- SELECT a.Unique_Identifier, b.Unique_Identifier
  -- --INTO a_id, b_id
  -- FROM api_mymodel a
  -- JOIN api_mymodel b ON a.Unique_Identifier <> b.Unique_Identifier
  -- WHERE a.open_or_close = 'Open'
  --   AND b.open_or_close = 'Open'
  --   AND a.player_pref = 'Any'
  --   AND b.player_pref = 'Any'
  --   AND a.match_pref = 'Any'
  --   And b.match_pref = 'Any'
  -- ORDER BY a.datetime, b.datetime
  -- LIMIT 1;
  --Set open_or_close = 'Close'
  --Where open_or_close = 'Open' 
  




CREATE EVENT UpdateMatches
ON SCHEDULE EVERY 20 SECOND
DO
  BEGIN
  --ENABLE Below when in production
     UPDATE api_mymodel
     SET open_or_close = 'Suspended', SuspendMessageSent = NOW()
     WHERE open_or_close = 'Open' AND last_called < NOW() - INTERVAL 15 SECOND;

     UPDATE api_mymodel
     SET open_or_close = 'Closed'
     WHERE open_or_close = 'Suspended' AND last_called < NOW() - INTERVAL 300 SECOND;


    UPDATE api_mymodel x 
    JOIN (
      SELECT a.Unique_Identifier AS 'Unique_Identifier', b.Unique_Identifier AS 'Opponent_Unique_Identifier'
      FROM api_mymodel a
      JOIN api_mymodel b ON a.Unique_Identifier <> b.Unique_Identifier
      WHERE 
      a.open_or_close = 'Open'
      AND 
      b.open_or_close = 'Open'
        
        AND 
        --Players = Players AND Teams = Teams
        ((a.player_numb = b.player_numb
        AND 
        a.team_league = b.team_league) 
        OR
        --Same League match Any Players
        (a.player_pref = 'ANY' AND (b.player_pref = 'ANY' OR a.player_numb = b.player_numb)
        AND 
        a.team_league = b.team_league
        AND a.match_pref = 'Current') 
        
        OR
        --Same players match Any League
        (a.player_numb = b.player_numb 
        AND 
        a.match_pref = 'Any' AND (b.match_pref = 'Any' OR a.team_league = b.team_league)) 
        
        OR
        (a.player_pref = 'Any'
        AND b.player_pref = 'Any'
        AND a.match_pref = 'Any'
        AND b.match_pref = 'Any'))
        
      ORDER BY a.datetime, b.datetime
      LIMIT 1
    ) y ON x.Unique_Identifier = y.Unique_Identifier
    SET x.Opponent_Unique_Identifier = y.Opponent_Unique_Identifier;

    --Flip a coin and store the results as a variable
    SET @result = (SELECT IF(RAND() < 0.5, 'heads', 'tails'));

    
    UPDATE api_mymodel a 
    JOIN api_mymodel b ON a.Opponent_Unique_Identifier = b.Unique_Identifier
    SET a.opponent_manager = b.player_name, a.opponent_team = b.team_name, a.open_or_close = 'Close',
    a.send_v_receive = Case WHEN @result = 'heads' THEN 'Send' ELSE 'Receive' END
    WHERE a.open_or_close = 'Open';


    UPDATE api_mymodel a 
    JOIN api_mymodel b ON a.Unique_Identifier = b.Opponent_Unique_Identifier
    SET a.Opponent_Unique_Identifier = b.Unique_Identifier, a.opponent_manager = b.player_name, a.opponent_team = b.team_name, a.open_or_close = 'Close',
    a.send_v_receive = Case WHEN @result = 'tails' THEN 'Send' ELSE 'Receive' END
    WHERE a.open_or_close = 'Open';
  END;


--DROP TRIGGER my_trigger;

-- CREATE TRIGGER my_trigger AFTER INSERT ON api_mymodel
-- FOR EACH ROW
-- BEGIN
--   CALL mysql.UpdateMatches;
-- END;



SELECT Unique_Identifier,open_or_close,team_name,team_league,player_numb,player_pref, match_pref,send_v_receive,'|',opponent_team,Opponent_Unique_Identifier,last_called  FROM api_mymodel LIMIT 100;


SELECT * FROM api_mymodel LIMIT 100;