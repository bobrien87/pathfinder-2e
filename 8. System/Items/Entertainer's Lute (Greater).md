---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Coda]]", "[[Occult]]", "[[Staff]]"]
price: "{'gp': 460}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This lustrous lute has a polished body and frets inlaid with mother of pearl. The decorations on the lute transform to show whatever decorations or carvings you find most appealing, and they change further to reinforce the story of the song you're currently playing. Its frets are inlaid with mother of pearl. With its mix of compelling illusions and mental tricks, it's favored by many traveling minstrels. While playing the lute, you gain a +1 item bonus to Diplomacy and Performance checks.

**Activate** Cast a Spell

**Effect** You expend a number of charges from this instrument to cast a spell from its list.

- **Cantrip** [[Infectious Enthusiasm]]
- **1st** [[Bless]], [[Ventriloquism]]
- **2nd** [[Calm]], [[Phantasmal Treasure]]
- **3rd** [[Enthrall]], [[Heroism]], [[Illusory Creature]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
