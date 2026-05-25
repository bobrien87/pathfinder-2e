---
type: deity
source-type: "Remaster"
domains: "Indulgence, Knowledge, Undeath, Vigil"
favored-weapon: "Jaws, Flail"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Jump]], Rank 2: [[Expeditious Excavation]], Rank 3: [[Paralyze]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Kabriri, Him Who Gnaws, is the demon lord of ghouls, graves, and secrets kept by the dead. According to legend, Kabriri is the reborn form of the first humanoid to ever devour his kin in life. His realm, Everglut, is connected to graveyards throughout the multiverse by a snarled network of tunnels that bring knowledge and sacrifices to the demon lord. Kabriri appears as a hulking ghoul with elven ears, teeth filed to points, an unnaturally long tongue, ashen skin, and cloven hooves. He is worshipped primarily by ghouls and ghasts.

**Title** Him Who Gnaws

**Areas of Concern** Ghouls, graves, secrets kept by the dead

**Edicts** Eat the flesh of your own kind

**Anathema** Reveal secrets of the dead to nonbelievers, despoil grave markers

**Religious Symbol** skull bowl of maggots

**Sacred Animal** grave worms

**Sacred Colors** blue, ivory

**Source:** `= this.source` (`= this.source-type`)
