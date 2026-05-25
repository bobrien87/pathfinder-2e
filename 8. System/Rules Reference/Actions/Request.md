---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Mental]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You can make a request of a creature that's friendly or helpful to you. You must couch the request in terms that the target would accept given their current attitude toward you. The GM sets the DC of the Diplomacy check based on the difficulty of the request. Some requests are unsavory or impossible, and even a helpful NPC would never agree to them.
- **Critical Success** The target agrees to your request without qualifications.
- **Success** The target agrees to your request, but they might demand added provisions or alterations to the request.
- **Failure** The target refuses the request, though they might propose an alternative that is less extreme.
- **Critical Failure** Not only does the target refuse the request, but their attitude toward you decreases by one step due to the temerity of the request.

**Source:** `= this.source` (`= this.source-type`)
