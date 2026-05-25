---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Clockwork]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 20000}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Paper-thin interlocking gears and winding cogs make up this bronze *clockwork cloak*.

**Activate** `pf2:r` (manipulate)

**Frequency** once per day

**Trigger** You're struck by a melee attack with a held weapon

**Effect** The folds of the cloak attempt to divert the attack and catch the weapon in the cloak's gears. Make an Athletics check to [[Disarm]] the attacking creature.

**Activate** `pf2:2` (manipulate)

**Effect** You wrap the cloak around yourself and the winding gears decelerate your body, causing you to enter standby mode. While in standby mode you don't need to eat, drink, or sleep. You remain aware of your surroundings but take a –4 penalty to Perception checks. You can stay in standby mode indefinitely, although your body ages normally. You can leave standby mode as a free action. If you do so to initiate combat, you gain a +2 item bonus to your initiative roll.

> [!danger] Effect: Clockwork Cloak

**Source:** `= this.source` (`= this.source-type`)
