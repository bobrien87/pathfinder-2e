---
type: deity
source-type: "Remaster"
domains: "Might, Nature, Dreams, Earth"
favored-weapon: "Shield-boss"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 3: [[One With Stone]], Rank 5: [[Dreaming Potential]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Whereas most green men actively evade humanoids, Granduncle Taproot escapes notice because he's usually buried deep underground. There he can slumber for ages at a time. When he does rouse, he wanders in a daze, marveling at the strange creatures that have arrived or evolved since he last stretched his legs. Yet should he emerge in a city or other landscape bereft of natural beauty, his wrath is terrible indeed. Granduncle Taproot has skin like that of a wizened potato, and thousands of tiny roots give him the appearance of a long, wispy beard. When he finally burrows down to sleep, it's not just to regain strength; it's an opportunity to dream and reflect on everything he witnessed and ponder deep thoughts. Those who revere Granduncle Taproot likewise value their rest, insisting on ample sleep and downtime to think. While awake, these followers work industriously, ensuring that no contributor to their projects goes unrewarded or unappreciated. After all, it's all too easy to praise a tree while overlooking the roots that keep it upright. Granduncle Taproot rarely meets his disciples. Instead, his body sometimes sends sprouts up to the surface to form a wondrous garden of unfamiliar fruits. Those who feast on the bounty absorb a fragment of the green man's thoughts, which echo in the eater's dreams for weeks afterward. Those who embrace these visions can learn from Granduncle Taproot, becoming one of his faithful.

**Title** He Who Hides in Humus

**Areas of Concern** Rest, roots

**Edicts** Honor those whose essential work is overlooked, preserve areas of natural wilderness, relish your well-deserved rest

**Anathema** Harm a sleeping creature, harm plant life except in the pursuit of saving greater plant life

**Religious Symbol** wood knot resembling a closed eye

**Sacred Animal** bear

**Sacred Colors** brown, green

**Source:** `= this.source` (`= this.source-type`)
