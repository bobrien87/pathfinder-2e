---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 360}"
usage: "worn"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The soles of these plain leather boots look like coils of flattened roots. The boots allow for fullfoot flexibility despite their sturdy make and smell faintly of evergreen trees. While worn and invested, your footsteps sound like rustling leaves, granting you a +1 item bonus to Stealth checks in a forest or wooded area.

**Activate—Root Walk** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The small roots extending from the soles of these boots allow you to move freely and easily across wood. For 10 minutes, you gain a 20-foot climb Speed on trees and other wooden surfaces, and you don't need to use your hands to climb.

> [!danger] Effect: Root Boots

**Activate—Take Root** `pf2:r` (concentrate)

**Frequency** once per day

**Trigger** You're standing on earth, and something attempts to move you against your will

**Effect** The roots extend from your boots to grip the ground, granting you a +4 item bonus to your Fortitude DC against effects that attempt to move you, such as [[Shove]] or Pull.

**Source:** `= this.source` (`= this.source-type`)
