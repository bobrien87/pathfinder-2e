---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 360}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This silver disc displays an ever-changing etching of an animal. When you affix the *beastmaster's sigil*, the animal settles into a single form based on where you affix it, showing the animal the item can summon when affixed that way. The spell DC of any spell cast by activating this item is 23. A weapon can benefit from only the melee weapon benefit or ranged weapon benefit. A thrown melee weapon gets the melee weapon benefit, and a combination weapon gets only one benefit, which you choose when you affix the spellheart. If it's unclear which one should apply, the GM decides.

- **Armor** The sigil grants you a +1 item bonus to saving throws against poison.
- **Melee Weapon** The sigil grants you a +1 item bonus to Athletics checks to [[Trip]].
- **Ranged Weapon** If you critically hit with the affixed weapon, and the target is adjacent to a creature summoned with the sigil, the target takes 2d6 persistent bleed damage.

> [!danger] Effect: Beastmaster's Sigil   Armor

> [!danger] Effect: Beastmaster's Sigil   Melee Weapon

> [!danger] Effect: Beastmaster's Sigil   Ranged Weapon

**Activate** Cast a Spell

**Effect** You cast [[Tame]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 3rd-rank [[Summon Animal]] to summon a [[Giant Monitor Lizard]] (armor), [[Boar]] (melee), or [[Giant Bat]] (ranged).

**Source:** `= this.source` (`= this.source-type`)
