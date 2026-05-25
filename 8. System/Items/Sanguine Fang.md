---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Spellheart]]", "[[Void]]"]
price: "{'gp': 650}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A pointed vampire fang hovers within this smoked-glass vial, its tip crimson with slowly dripping blood. The spell DC of any spell cast by activating this item is 25.

- **Armor** You gain resistance 3 to persistent bleed damage and a +2 item bonus on saving throws against effects with the void trait.
- **Weapon** After you cast a spell by activating the *fang*, your Strikes with the weapon deal 1d4 persistent bleed damage until the end of your next turn.

> [!danger] Effect: Sanguine Fang   Armor

> [!danger] Effect: Sanguine Fang   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Void Warp]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Vampiric Feast]].

**Source:** `= this.source` (`= this.source-type`)
