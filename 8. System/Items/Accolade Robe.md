---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Arcane]]", "[[Focused]]", "[[Invested]]"]
price: "{'gp': 1000}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Although not all wizards have gone through formal training, it's become tradition to enchant robes representing the arduous training required and festoon them with honors one has earned. Typically, an *accolade robe* is styled after a single wizard school, with appropriate colors and symbols. Wearing these robes grants a +2 item bonus to Arcana checks.

The pockets of the robe tie to an extradimensional space that can hold 1 Bulk of items, none of which can have greater than light Bulk. The items must be related to spellcasting and academics—spellbooks, scrolls, wands, scholarly journals, and other academic supplies the GM allows. These items do not count against your Bulk limit. You can Interact to retrieve or stow items normally.

**Activate—Review** `pf2:1` (concentrate, manipulate)

**Effect** You retrieve an item of your choice from the robe's storage, then Recall Knowledge.

**Activate—Extra Credit** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can spend only to cast a school spell. If you don't spend this Focus Point by the end of this turn, it is lost.

**Craft Requirements** You are a wizard of the associated school.

**Source:** `= this.source` (`= this.source-type`)
