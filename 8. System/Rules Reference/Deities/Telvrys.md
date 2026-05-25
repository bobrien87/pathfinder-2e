---
type: deity
source-type: "Remaster"
domains: "Might, Nature, Destruction, Travel"
favored-weapon: "Earthbreaker"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 2: [[Acid Grip]], Rank 6: [[Tangling Creepers]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Lush valleys, primeval rainforests, and prairies whose deep roots scrape the bedrock—these fertile lands would not exist if not for Telvrys. To him, every mountaintop and cooling lava flow is a potential garden if properly prepared. Using lichens and hardy sprouts, he patiently oversees erosion and colonizes barren rock with soil. However, once the tiny garden is self-sustaining, Telvrys has already departed in search of higher peaks and more hostile realms to reclaim.

Telvrys resembles a kappa made of moss and gravel, with hardy shrubs growing from his stooped back and dark soil brimming from a shallow divot atop his head. He often carries a knobby walking stick covered in burrs and seed cases that fall free each time he taps the ground. He has no permanent region, instead ranging across Golarion as he's inspired. He's known to spend years at a time fruitlessly colonizing sand-blasted peaks, only to depart in a terrible mood.

Though he doesn't seek out humanoids, Telvrys can't help but marvel at anyone who would brave the mountains; those who impress him can earn his aid, be that his saving them from a fall or even adopting them as apprentices.

Of all the green man faiths, Telvrys's disciples are the most mobile, often falling in with adventuring groups traveling to high-altitude areas, taking time to transplant seedlings into sheltered niches. These wanderers share a special bond with followers of Irori, Kurgess, Yamatsumi, and other deities of athleticism, finding joy in how each explorer can collaborate in scaling mountains for different yet complementary reasons.

**Title** The Soilcrown

**Areas of Concern** Mountain climbing, primary plant growth, stubbornness

**Edicts** Sow new life in desolate places, foster the growth and well-being of flora, patiently mentor disciples, climb to high places

**Anathema** Abandon an endeavor before making a stubborn attempt, harm fragile ecosystems except in the pursuit of saving greater plant life, demean those who attempt difficult tasks

**Religious Symbol** sprout on a mountain's peak

**Sacred Animal** bee

**Sacred Colors** green, white

**Source:** `= this.source` (`= this.source-type`)
