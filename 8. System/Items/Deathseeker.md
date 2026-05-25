---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Agile]]", "[[Deadly d8]]", "[[Finesse]]", "[[Magical]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A hauntingly beautiful and masterfully crafted blade, this *+1 striking wounding kris* has been whet with the spilled blood of its creator, imbuing violent intent within its crimson curves. When you critically succeed at a Strike made with a deathseeker, the target feels the blade's unbridled bloodlust trying to consume it and must attempt a DC 24 [[Will]] save; this effect has the incapacitation trait.
- **Critical Success** The target is unaffected and is temporarily immune for 24 hours.
- **Success** The target takes an additional 1 persistent bleed damage, and the DC for recovering from persistent bleed damage is 17, or 12 with particularly effective assistance.
- **Failure** As success, except the target is also [[Confused]] for 1 round. It gets a flat check to recover from this confusion when it critically succeeds at a Strike against another creature or reduces another living being to 0 Hit Points, but not when it takes damage.
- **Critical Failure** As success, except the target is also confused for 3 rounds. It gets a flat check to recover from this confusion when it critically succeeds at a Strike against another creature or reduces another living being to 0 Hit Points, but not when it takes damage.

**Source:** `= this.source` (`= this.source-type`)
