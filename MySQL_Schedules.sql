
SHOW EVENTS;


DROP EVENT UpdateClosedEntries;


  
  SELECT a.Unique_Identifier, b.Unique_Identifier
  --INTO a_id, b_id
  FROM api_mymodel a
  JOIN api_mymodel b ON a.Unique_Identifier <> b.Unique_Identifier
  WHERE a.open_or_close = 'Open'
    AND b.open_or_close = 'Open'
    AND a.player_pref = 'Any'
    AND b.player_pref = 'Any'
    AND a.match_pref = 'Any'
    And b.match_pref = 'Any'
  ORDER BY a.datetime, b.datetime
  LIMIT 1;
  --Set open_or_close = 'Close'
  --Where open_or_close = 'Open' 
  

CREATE EVENT UpdateClosedEntries
ON SCHEDULE EVERY 15 SECOND
DO
BEGIN
  UPDATE api_mymodel
  SET open_or_close = 'Close'
  WHERE open_or_close = 'Open' AND last_called < NOW() - INTERVAL 10 SECOND;

  UPDATE api_mymodel x 
  JOIN (
    SELECT a.Unique_Identifier AS 'Unique_Identifier', b.Unique_Identifier AS 'Opponent_Unique_Identifier'
    FROM api_mymodel a
    JOIN api_mymodel b ON a.Unique_Identifier <> b.Unique_Identifier
    WHERE a.open_or_close = 'Open'
      AND b.open_or_close = 'Open'
      AND a.player_pref = 'Any'
      AND b.player_pref = 'Any'
      AND a.match_pref = 'Any'
      AND b.match_pref = 'Any'
    ORDER BY a.datetime, b.datetime
    LIMIT 1
  ) y ON x.Unique_Identifier = y.Unique_Identifier
  SET x.Opponent_Unique_Identifier = y.Opponent_Unique_Identifier;


  UPDATE api_mymodel a 
  JOIN api_mymodel b ON a.Opponent_Unique_Identifier = b.Unique_Identifier
  SET a.opponent_manager = b.player_name, a.opponent_team = b.team_name, a.open_or_close = 'Close';


  UPDATE api_mymodel a 
  JOIN api_mymodel b ON a.Unique_Identifier = b.Opponent_Unique_Identifier
  SET a.Opponent_Unique_Identifier = b.Unique_Identifier, a.opponent_manager = b.player_name, a.opponent_team = b.team_name, a.open_or_close = 'Close';
END;

    



