---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]", "[[Metal]]", "[[Spellheart]]"]
price: "{'gp': 90}"
usage: "affixed-to-metal-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This perfectly octahedral magnetite crystal is covered in a hair-like layer of iron sand that always finds its way back to shape if wiped away. The spell attack modifier of any spell cast by Activating this item is +8, and the spell DC is 18.

- **Armor** You gain a +1 item bonus to Athletics checks and resistance 2 to nonlethal damage.

- **Weapon** After you cast a spell by Activating the *spiny lodestone*, your Strikes with the weapon deal an additional 1d4 piercing damage until the end of your next turn.

> [!danger] Effect: Spiny Lodestone   Armor

> [!danger] Effect: Spiny Lodestone   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Needle Darts]]

**Source:** `= this.source` (`= this.source-type`)
