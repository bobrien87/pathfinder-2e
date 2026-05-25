---
type: deity
source-type: "Remaster"
domains: "Introspection, Magic, Travel, Trickery"
favored-weapon: "Rapier"
divine-font: "Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 5: [[Illusory Scene]], Rank 7: [[True Target]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

As the trickster god of the cloud giants, Skrymir is the very embodiment of wanderlust, mischievousness, and acuity. Nearly always masquerading as a new persona whenever he's seen, he meanders the lands, rewarding those who correctly answer his riddles and pass his tests of wit. He has a familial connection with Bergelmir, but whether it is as her brother, cousin, or son differs from myth to myth, likely due in no small part to his love of disguises and lighthearted chicanery. Because of his tendency to change his appearance and presentation at a whim, frequently slipping into whatever form feels most comfortable at that moment in time, there are no consistent depictions of him. He could be a frail, blithering old man one moment, then a strong inquisitive young woman the next. He is always a giant of some kind, and the excited glint in his eye when he meets someone with sharp wit and a curious mind seems to carry over regardless of the form he takes.

**Title** The Seeker of Sunsets

**Areas of Concern** Riddles, wanderlust, wit

**Edicts** Seek out and explore unfamiliar places, use wit over violence whenever possible, lift spirits with harmless jokes and pranks

**Anathema** Settle down in one place for too long, harm someone with your jokes or pranks, turn down the chance to solve a riddle

**Religious Symbol** coastline pierced by blades

**Sacred Animal** octopus

**Sacred Colors** brown, silver

**Source:** `= this.source` (`= this.source-type`)
