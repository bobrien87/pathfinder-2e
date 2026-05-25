---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Grimoire]]", "[[Illusion]]", "[[Magical]]"]
price: "{'gp': 1250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Goblin wizards invented the amazing pop-up book to store their spells without written words, though the tradition has been spreading to illusionists from other cultures. These grimoires have colorful covers and open to reveal three-dimensional scenes illustrating various spells. Goblins delight in constructing the books just right so a terrifying creature, like a horse or dog, pops up toward the reader each time a page is turned.

**Activate** `pf2:f` (concentrate, spellshape)

**Frequency** once per day

**Effect** If your next action is to cast an illusion spell prepared from this grimoire that creates illusory terrain or creatures, such as [[Mirage]], you draw forth the pop-up scene. If a creature succeeds, but doesn't critically succeed, at a saving throw to disbelieve the illusion, then just as their mind recognizes the illusion, a startling—though obviously false—illusion pops up somewhere unexpected in their field of vision, visible to only them, dealing mental damage equal to the spell's rank.

**Source:** `= this.source` (`= this.source-type`)
