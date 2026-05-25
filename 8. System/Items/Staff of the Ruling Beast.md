---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Monk]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The Staff of the Ruling Beast appears as though it's made of myriad organic materials crudely woven together, from sinew and hide to bone and scales. The staff serves as a ceremonial sign of Iapholi's authority, and on rare occasions, she loans it to favored allies to speak in her name. Even then, she expects the staff will be returned at the task's conclusion, sending ferocious bounty hunters to retrieve it, if necessary.

**Activate—Overwhelming Sound** `pf2:2` (auditory, manipulate)

**Effect** With three sharp taps on the ground, the Staff of the Ruling Beast casts [[Bullhorn]] as a 5th-rank cantrip, affecting you so long as you hold the staff. While affected, you can make your words rumble with palpable force, allowing creatures (including those who cannot hear) to feel your speech and identify your location as if they were using an imprecise sense.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Concordant Choir]]
- **1st** [[Command]], [[Ventriloquism]]
- **2nd** [[Blistering Invective]], [[Calm]]
- **3rd** [[Dream Message]], [[Enthrall]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
