---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 55}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

When used to cast [[Breathe Fire]] or [[Chilling Spray]], a scale from a dragon's throat changes the spell's damage type and corresponding trait to the damage type and trait of the dragon's breath. You can instead choose the damage type and trait corresponding to the dragon's tradition if it's different.

> [!danger] Effect: Dragon Breath Scale

**Adamantine** bludgeoning or fire

**Conspirator** mental or poison

**Diabolic** fire or spirit

**Empyreal** spirit

**Fortune** force

**Horned** fire or poison

**Mirage** force or mental

**Omen** mental

**Source:** `= this.source` (`= this.source-type`)
