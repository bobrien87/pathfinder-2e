---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Divine]]", "[[Spellheart]]"]
price: "{'gp': 1750}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This spellheart is fashioned from the tip of a demon's horn that's been polished until smooth and shiny. The spell DC of any spell cast by Activating this item is 29.

- **Armor** You gain resistance 10 to unholy.
- **Weapon** After you cast an enchantment spell by Activating the *horn*, your Strikes with the weapon deal an additional 1d8 mental damage until end of your next turn.

> [!danger] Effect: Polished Demon Horn   Armor

> [!danger] Effect: Polished Demon Horn   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Daze]] (DC 29 [[Will]] save).

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 3rd-rank [[Fear]] (DC 29 [[Will]] save)..

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Outcast's Curse]] (DC 29 [[Will]] save).

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Vision of Death]] (DC 29 [[Will]] save).

**Source:** `= this.source` (`= this.source-type`)
