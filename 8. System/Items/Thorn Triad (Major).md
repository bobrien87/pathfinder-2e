---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Spellheart]]", "[[Wood]]"]
price: "{'gp': 1800}"
usage: "affixed-to-non-metal-armor-or-a-weapon"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

From each corner of this carved, triangular badge extends a long, sharp thorn. The spell DC of any spell cast by activating this item is 29.

- **Armor** After you cast a plant spell by activating the triad, you gain resistance 6 to bludgeoning and piercing damage and weakness 3 to fire until the end of your next turn, or double the resistance for a non-cantrip spell.
- **Weapon** After you cast a plant spell by activating the triad, thorns erupt from the weapon. Your Strikes with the weapon deal an additional 1d8 persistent bleed damage until the end of your next turn.

> [!danger] Effect: Thorn Triad   Armor

> [!danger] Effect: Thorn Triad   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Timber]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 4th-rank [[Wall of Thorns]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Petal Storm]].

**Source:** `= this.source` (`= this.source-type`)
