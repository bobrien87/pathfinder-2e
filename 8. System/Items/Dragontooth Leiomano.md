---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Fatal d10]]", "[[Versatile s]]"]
price: "{'gp': 3000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Dragon teeth line the edges of this +2 greater striking leiomano. The leiomano deals an additional @Damage[1d6[untyped]|options:area-damage] damage of a type determined by the tradition of the dragon from which the teeth were taken: force for arcane, spirit for divine, mental for occult, or fire for primal. The weapon also gains the relevant trait (for instance, fire for a club made with teeth taken from an adamantine dragon).

**Activate** `pf2:2` (magical, manipulate)

**Frequency** once per minute

**Effect** You swing the leiomano, sending several of the dragon teeth shooting through the air on jets of energy. The dragon teeth deal @Damage[3d6[piercing]|options:area-damage] damage and @Damage[3d6[untyped]|options:area-damage] damage of the damage type corresponding to the dragon's tradition in a @Template[type:cone|distance:15] (DC 29 [[Reflex]] save). The teeth hunt down their targets, correcting their flight in midair, which reduces any circumstance bonus from cover by 2.

**Craft Requirements** The initial raw materials must include teeth from a dragon.

**Source:** `= this.source` (`= this.source-type`)
