---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Consumable]]", "[[Fortune]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 14000}"
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

A liquid with the appearance of an expressive night sky and a taste that's sheer pleasure, starsong nectar grants you cheerful confidence and incredible luck for 10 minutes after you drink it. However, if you show too much caution at any point during this time (GM's discretion), you must succeed at a DC 6 flat check or the potion's effects end. While the potion lasts, you gain a +3 status bonus to attack rolls, initiative rolls, Perception checks, saving throws, and skill checks, and you aren't [[Off Guard]] to creatures due to them flanking you or being [[Hidden]] from or [[Undetected]] by you. You are temporarily immune to this potion for 24 hours once its effects end.

While the potion lasts, though, if you take a moment to imagine the future, you choose the best courses of action. This aspect of the potion grants you the following activation.

**Activate** `pf2:1` (concentrate)

**Frequency** once per round

**Effect** Until the start of your next turn, roll two d20s for any attack rolls, Perception checks, saving throws, and skill checks you make and take the higher result.

> [!danger] Effect: Starsong Nectar

**Source:** `= this.source` (`= this.source-type`)
