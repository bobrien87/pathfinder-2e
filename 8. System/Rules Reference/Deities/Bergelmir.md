---
type: deity
source-type: "Remaster"
domains: "Family, Knowledge, Repose, Vigil"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Déjà Vu]], Rank 3: [[Hypercognition]], Rank 4: [[Rewrite Memory]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Bergelmir is primarily worshipped by cloud and stone giants, though many humans in the Realm of the Mammoth Lords have devoted themselves to her as well. She is related to Skrymir, but the manner in which they are family constantly differs depending on the tale being told and its storyteller. Some say they are siblings, others say they are cousins, and just as many interpret them as mother and son. Regardless, as the goddess of family, elders, and genealogy, Bergelmir chronicles the lives and lineages of giant families and records their births and deaths in a colossal tome. Any histories, songs, stories, or rituals passed on by mouth or written word is remembered and immortalized by her, save for very few exceptions.

**Title** Mother of Memories

**Areas of Concern** Elders, family, genealogy, memories, tradition

**Edicts** Learn the traditions and history of your people, care for the elderly, share your wisdom and knowledge

**Anathema** Destroy historical texts or records, alter or obfuscate oral histories, harm the elderly

**Religious Symbol** Three bolts of lightning

**Sacred Animal** sea turtle

**Sacred Colors** gray, white

**Source:** `= this.source` (`= this.source-type`)
