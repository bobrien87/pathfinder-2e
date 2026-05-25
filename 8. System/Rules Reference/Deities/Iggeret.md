---
type: deity
source-type: "Remaster"
domains: "Darkness, Void, Protection, Sorrow"
favored-weapon: "Shortbow"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 4: [[Vision Of Death]], Rank 7: [[Project Image]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Curiously, Iggeret has claimed that she was once a mortal girl who faked her own kidnapping to see how her family would react. After her parents killed themselves out of despair, She Who Was Lost entombed herself with their bodies, eventually joining them in death. None can confirm or deny this story. As a sahkil tormentor, Iggeret holds sway over dark and empty places such as pits and graves. She considers all who dwell in darkness to be her new family, and that they should join her in death. She Who Was Lost appears as a young girl with a gaunt, skeletal face and long, black hair. She weeps constant tears that stain her cheeks and simple white dress

**Title** She Who Was Lost

**Areas of Concern** Darkness, empty places, pits

**Edicts** Divest yourself of possessions and relationships whenever possible, foment despair and sorrow, rest among the dead

**Anathema** Fear the dark, grow too fond of your possessions and relationships

**Religious Symbol** disused well

**Sacred Animal** rabbit

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
