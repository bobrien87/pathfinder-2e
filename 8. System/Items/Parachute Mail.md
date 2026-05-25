---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Flexible]]", "[[Invested]]", "[[Magical]]", "[[Noisy]]"]
price: "{'gp': 150}"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Favored by soldiers deployed on airships, this chain mail has a built-in parachute connected to the armor itself, with an additional harness to be worn underneath. It takes 10 minutes and a successful DC 15 [[Crafting]] check to successfully repack the parachute.

**Activate—Deploy Parachute** `pf2:r` (manipulate)

**Frequency** once until repacked

**Trigger** You are falling

**Effect** Once activated, the parachute will fully deploy within 1 round. If it is deployed at a height greater than 100 feet, the parachute will prevent you from receiving falling damage. If deployed at a height of less than 100 feet, it will reduce the damage taken from falling by half.

**Source:** `= this.source` (`= this.source-type`)
