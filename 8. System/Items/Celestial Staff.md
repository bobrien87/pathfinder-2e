---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Holy]]", "[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 14000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Heavenly radiance shines from an active *celestial staff*, a golden staff capped with a pair of sculpted angel's wings. Used as a weapon, the staff is a *+2 greater striking holy staff*. While wielding a *celestial staff*, you gain a +1 circumstance bonus to saving throws against effects that have the unholy trait and effects created by unholy creatures. When you prepare this staff, if you're unholy, you become [[Drained]] 1 until your next daily preparations.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Divine Lance]]
- **1st** [[Bless]], [[Protection]]
- **2nd** [[Everlight]], [[Inner Radiance Torrent]]
- **3rd** [[Anointed Ground]], [[Protection]]
- **4th** [[Holy Cascade]], [[Inner Radiance Torrent]]
- **5th** [[Spiritual Guardian]], [[Summon Celestial]]
- **6th** [[Holy Cascade]], [[Summon Celestial]]
- **7th** [[Frigid Flurry]], [[Howling Blizzard]]

**Craft Requirements** You're holy. Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
