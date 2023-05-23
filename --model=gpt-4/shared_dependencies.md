the app is: Revised Political Campaign CRM Program

the files we have decided to generate are: main.py, utils.py, data.txt, output.txt

Shared dependencies between the files:

1. Exported variables:
   - Google Geocode API key: `AIzaSyDM5zZdZCOfguxHyDESvEhzxVJIOeqmGto`
   - Google Map API Key: `AIzaSyDM5zZdZCOfguxHyDESvEhzxVJIOeqmGto`

2. Data schemas:
   - Voter schema: Voter ID, Full Name, Date of Birth, Phone Number, Email, Instagram, Facebook, Key Issues, Data Consent, Address, Location, Referral, Vote Intent
   - Voter Request schema: Request ID, Name, Description, Associated Voter, Date Submitted, Location, Status

3. DOM element id names:
   - voterList (Voter List View)
   - referralList (Track Referrals)
   - requestList (Request List)
   - kanbanView (Kanban View)
   - mapView (Map View)

4. Message names:
   - addVoter
   - updateVoter
   - deleteVoter
   - addRequest
   - updateRequest
   - deleteRequest

5. Function names:
   - createVoter
   - readVoter
   - updateVoter
   - deleteVoter
   - createRequest
   - readRequest
   - updateRequest
   - deleteRequest
   - filterVoters
   - sortVoters
   - filterRequests
   - sortRequests
   - displayMapView
   - getVotersInRadius