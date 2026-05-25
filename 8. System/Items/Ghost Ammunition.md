---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]"]
price: "{'gp': 900}"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

*Ghost ammunition* is cool to the touch. This ammunition has the benefits of the *[[Ghost Touch]]* property rune and can fly through any obstacle except those that can block incorporeal creatures or effects. Though the ammunition penetrates barriers and ignores all cover, the target still benefits from the flat check from being concealed or hidden. You still can't target an undetected creature without guessing.

After it is launched, the ammunition vanishes into mist. However, in the dead of the night 1d4 days later, it reappears in the last quiver or other container it was taken from.

**Source:** `= this.source` (`= this.source-type`)
