---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate) or 1 or more days; see below

An alchemist with the [[Craft Philosopher's Stone]] feat adds the formula for this item to their formula book. This allows them to create a philosopher's stone once per month during their daily preparations using advanced alchemy. Unlike other items created with advanced alchemy, the philosopher's stone remains potent for 1 month or until the alchemist creates a new one. This is the only way to create a philosopher's stone.

At a glance, a philosopher's stone appears to be an ordinary, sooty piece of natural rock. Breaking the rock open with a [[Force Open]] action (DC 35) reveals a cavity at the stone's heart. The cavity is lined with a rare type of quicksilver that can transmute base metals into precious metals or create an elixir of rejuvenation.

To use the quicksilver, you must be legendary in Crafting and have the Alchemical Crafting feat. You can then use the stone's quicksilver for one of two effects.

- You can apply the stone's quicksilver to an infused [[Elixir of Life (True)]] using an Interact action. This turns the elixir into an infused [[Elixir of Rejuvenation]] instantaneously. This doesn't require any crafting time or additional materials.
- You can spend up to a month of downtime applying the quicksilver either to iron to create silver or to lead to create gold. Treat this as a 20th-level task to [[Earn Income]] using Crafting, except that you create 500 gp worth of your chosen metal per day on a success or 750 gp worth per day on a critical success.

**Source:** `= this.source` (`= this.source-type`)
