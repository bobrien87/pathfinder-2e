---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 625}"
bulk: "4"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An image of a keyhole adorns the coat of arms of this stone tower shield (Hardness 10, HP 40, BT 20).

**Activate** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** The shield becomes a locked door in an empty, adjacent space no wider than 5 feet, becoming flush with the surrounding structure so it blocks all passage. The door has the same Hardness, HP, and Broken Threshold as the shield, with DC 25 [[Athletics]] check and DC 25 [[Thievery]] check to open. The door remains in place for 1 hour, until it's opened or broken, or until you spend an action to end this effect, at which point the shield returns to your hand (or falls to the ground in your space if your hands are full).

**Activate** 1 minute (concentrate)

**Frequency** once per day

**Effect** The shield floats lazily in the air as bricks quickly fly from it to form a squat stone tower around it. You cast [[Cozy Cabin]], with the shield becoming the door.

**Source:** `= this.source` (`= this.source-type`)
