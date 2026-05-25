---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 210}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** Member of a secret society

These large portraits are commonly commissioned by secret societies to display their current member ranks, and to protect against members who would break their vows to keep their secrets. Each member being painted gives their consent to be traced by the portrait, and they agree to keep their vows for as long as their membership stands or until death, whichever comes first. This consent can be transferred to a new portrait if one is needed once the society expands, without needing another confirmation.

Should a member betray the secrets of their society, their image in the society portrait changes within 10 minutes, altering the image of the member by spelling out "TRAITOR" across their form. It provides no details on the specifics of the betrayal. The traitor can attempt a DC 30 [[Will]] save or DC 30 [[Deception]] check at the time they betrayed a secret to avoid the portrait revealing their treachery. The traitorous scrawl can be counteracted by dispel magic targeted at the portrait (counteract DC 20, counteract rank of 3).

**Source:** `= this.source` (`= this.source-type`)
