---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Coda]]", "[[Occult]]", "[[Staff]]"]
price: "{'gp': 10000}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This exquisite fiddle is perfectly carved and balanced to produce the purest sound while granting its player perfect balance and poise. It grants a +2 item bonus to Performance checks. If you're a master in Performance, while playing it you also gain a +1 status bonus to Reflex saves and a +1 item bonus to Dexterity-based skill checks. If you're legendary in Performance, the bonuses are +2.

When you [[Perform]] with the fiddle, you can choose to create a harsh and discordant note. You critically fail the Performance check, shred the strings of the fiddle, and create an 8th-rank [[Noise Blast]], with a @Template[emanation|distance:40] around you instead of a @Template[burst|distance:10]. The fiddle can't be played again until the strings are replaced at a cost of 200 gp.

**Activate** Cast a Spell

**Effect** You expend a number of charges from this instrument to cast a spell from its list.

- **Cantrips** [[Figment]], [[Light]], [[Message]]
- **1st** [[Command]]
- **2nd** [[Calm]], [[Revealing Light]]
- **3rd** [[Enthrall]]
- **4th** [[Honeyed Words]]
- **5th** [[Sending]]
- **6th** [[Calm]], [[Dominate]], [[Vibrant Pattern]]
- **7th** [[Dominate]], [[Mask of Terror]], [[True Target]], [[Vibrant Pattern]], [[Visions of Danger]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
