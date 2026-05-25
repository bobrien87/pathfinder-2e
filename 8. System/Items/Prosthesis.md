---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "worn"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A prosthesis replaces a missing or damaged body part. Typical prostheses include artificial feet, eyes, hands, and limbs, though a basic prosthesis can be designed as a replacement for any body part. Advancements in the prosthetic field mean that even the most basic of prostheses can provide the full range of functionality for a missing body part.

A prosthesis has a number of belts or cuffs that keep it attached to your body. You can attach or remove a prosthesis as an Interact action.

**Source:** `= this.source` (`= this.source-type`)
