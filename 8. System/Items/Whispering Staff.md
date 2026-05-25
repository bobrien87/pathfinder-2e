---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 70000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This gnarled wooden staff is carved with humanoid faces in various emotional states. When the staff is activated, the faces begin to whisper a variety of languages in sibilant tones, creating what seems to be nonsense to all but the staff's wielder or those they choose to affect. The staff functions as a Major Staff of the Unblinking Eye. While using the staff, you gain a +3 item bonus to Decipher Writing, Identify Magic, and Recall Knowledge checks, regardless of the skill. When you invest the staff, you either increase your Intelligence modifier by 1 or increase it to +4, whichever would give you a higher value. You must select the skills and languages the first time you invest the item, and whenever you invest the same whispering staff, you get the same skills and languages you chose the first time.

**Activate** `pf2:1` (concentrate, mental)

**Frequency** once per round

**Effect** Through the staff's strange whispering, you gain a glimpse into the mind and desires of one creature you can see within 30 feet. Until the end of your next turn, that creature is [[Off Guard]] to you and takes a –2 circumstance penalty to saving throws against your spells.

> [!danger] Effect: Whispering Staff (Enemy)

**Activate** `pf2:2` (manipulate, mental, misfortune)

**Frequency** once per hour

**Effect** You point the staff at one creature you can see within 30 feet of you, causing the whispers to howl in that creature's mind. The target must attempt a DC 43 [[Will]] save. If it fails, whenever the creature attempts an attack roll, skill check, or saving throw, it must roll twice and take the worse roll. This lasts until the start of your next turn.

**Activate** `pf2:2` (concentrate, fortune, mental)

**Frequency** once per day

**Effect** You twirl the staff in three consecutive circles and call for the whispers to speak up. For the next minute, you and all allies within a @Template[type:emanation|distance:30] around you can hear your staff's whispers clearly and distinctly, gaining benefit from their advice and mental protection. Whenever you and your affected allies attempt to Recall Knowledge or attempt a saving throw against a mental effect, you roll twice and take the better result. This is a fortune effect.

> [!danger] Effect: Whispering Staff (Ally)

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Detect Magic]]
- **1st** [[Sure Strike]]
- **2nd** [[Darkvision]], [[See the Unseen]], [[Translate]]
- **3rd** [[Darkvision]], [[Mind Reading]]
- **4th** [[Clairvoyance]], [[Detect Scrying]], [[Telepathy]]
- **5th** [[Mind Probe]], [[Scouting Eye]]
- **6th** [[Telepathy]], [[Truesight]]

**Source:** `= this.source` (`= this.source-type`)
