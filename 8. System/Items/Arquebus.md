---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concussive]]", "[[Fatal d12]]", "[[Kickback]]"]
price: "{'gp': 8}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This is a long gun that offers more range than the average firearm, though the long barrel and ferocious kickback make the weapon particularly unsteady unless a tripod or other stand is used to stabilize it. The arquebus is one of the most commonly used long guns among the soldiers of Dongun Hold and Alkenstar.

**Source:** `= this.source` (`= this.source-type`)
