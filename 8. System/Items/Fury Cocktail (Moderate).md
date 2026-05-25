---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 360}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A fury cocktail is a fortifying ginger beer spiked with rum and a mixer. It's rumored to have originated from a barbarian-themed festival in a popular mead hall specializing in alchemical beverages.

**Benefit** You gain a +3 item bonus to melee attack rolls and an additional effect depending on the additive chosen when the brew is created. The effects last 1 hour.

- **Animalistic** Lemon juice and powdered claws or talons are added to the cocktail. You gain an unarmed attack in the brawling group of your choice between a jaws attack that deals 1d6 piercing damage or a claw attack that has the agile trait and deals 1d4 slashing damage.
- **Double** This cocktail is just stronger, with more ginger and more rum. You gain resistance 2 to physical damage.
- **Mournful** A few flower petals add a powerful aroma to the drink. You gain resistance 5 to void damage, or resistance 5 to vitality damage if you have the void healing ability.
- **Skeptical** A splash of bitters gives the drink a more complex flavor. You gain a +2 item bonus to saves against magic.
- **Titanic** Yuzu juice and powdered giant hair are added to this cocktail. If you're Medium or smaller, you gain the following effects: you become Large, are [[Clumsy]] 1, and increase your reach by 5 feet (or by 10 feet if you started out Tiny).
- **Wyrmhide** Pomegranate juice and elemental reagents are added to the cocktail. You gain resistance 5 to acid, cold, electricity, fire, and poison damage.

**Drawback** You take a –1 penalty to AC and a –2 penalty to Reflex saves.

> [!danger] Effect: Fury Cocktail (Moderate)

**Source:** `= this.source` (`= this.source-type`)
