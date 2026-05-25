---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 700}"
usage: "etched-onto-thrown-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Able to copy itself many times over when thrown until the air is filled with deadly blades, a swarming weapon turns a single weapon into a shower of devastation.

**Activate** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** You fling your weapon and it multiplies as it flies through the air, filling a @Template[type:cone|distance:30]. All creatures within the area take damage equal to double the weapon's number of damage dice, with a DC 27 [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
