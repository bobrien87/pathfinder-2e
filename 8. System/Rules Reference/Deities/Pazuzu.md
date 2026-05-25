---
type: deity
source-type: "Remaster"
domains: "Air, Swarm, Trickery, Tyranny"
favored-weapon: "Longsword"
divine-font: "Harm"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 4: [[Aerial Form]], Rank 8: [[Migration]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Pazuzu, King of the Wind Demons, is the demon lord of the sky, temptation, and winged creatures. He counts himself among the most ancient of demon lords, though his constant warring with Lamashtu has hindered his accumulation of power to the point of denying him godhood. He is exceptionally active in meddling in mortal affairs and takes great pleasure in possessing and corrupting good-hearted folk who invoke his name. Pazuzu appears as a humanoid figure with eagle's talons, two pairs of bird wings, a scorpion tail, and an avian demonic head. He is worshipped by harpies, other evil winged creatures, and by countless champions and clerics who fell from grace at his temptations.

**Title** King of the Wind Demons

**Areas of Concern** The sky, temptation, winged creatures

**Edicts** Tempt others to immoral acts, revel in flight, possess or magically influence others to cause calamities

**Anathema** Deny a flying creature the ability to fly, abuse Pazuzu's name or call on Pazuzu for help, aid worshippers of Lamashtu

**Religious Symbol** himself, right hand raised

**Sacred Animal** all flying animals

**Sacred Colors** brown, red

**Source:** `= this.source` (`= this.source-type`)
