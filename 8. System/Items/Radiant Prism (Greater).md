---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 20500}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This glass prism pays homage to its namesake pantheon—the Radiant Prism of Sarenrae, Desna, and Shelyn. Any armor or weapon the prism is affixed to glows softly with colored lights. The spell DC of any spell cast by activating this item is 38.

- **Armor** (light) After you cast a non-cantrip spell by activating the prism, you glow with dim light in a multitude of shimmering hues, shedding light like a [[Torch]] and making you [[Concealed]] for 2 rounds.
- **Weapon** After you cast a non-cantrip spell by activating the prism, your Strikes with the weapon gain the [[Brilliant]] property rune until the end of your next turn. The damage from the *brilliant* rune increases to 2d4 of each type.

**Activate** Cast a Spell

**Effect** You cast [[Light]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Fiery Body]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Confusing Colors]].

**Source:** `= this.source` (`= this.source-type`)
