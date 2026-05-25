---
type: deity
source-type: "Remaster"
domains: "Air, Confidence, Might, Perfection"
favored-weapon: "Mace"
divine-font: "Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Shockwave]], Rank 3: [[Mad Monkeys]], Rank 4: [[Vapor Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

According to the teachings of Ragdya, at the center of the universe lies the great mountain of Bahmenu. It was upon these slopes that Ragdya was born and where he now again resides as the Sage on the Mountain. Ragdya spent much time in his younger days getting involved in the matters of the other Vudrani gods, giving rise to a repeating number of escapades featuring other deities such as Likha and Chamidu. In spite of his antics, Ragdya is much beloved, as he brings with him an infectious aura of mirth and excitement for all things in life.

Yet, for all the joy, there's also sorrow, for Ragdya sits alone watching over his progeny, the vanaras, and his faithful. He offers rebirth so his followers might come to better know themselves with continued experience, but in so doing, he can't have the happiness of holding his children close. Still, he wishes them to know the joy of love, to experience how the power of laughter can bond them with others regardless of station, and to hold their sorrows at bay for just a moment more. He wants them to know that there's no shame in learning a lesson borne from failure, but rather great pride in true humility and in being able to work past the ego to instead find humor in all the silly stages of life.

A common saying is that "a Ragdyan tries anything at least once, and gladly tells you the story of how it went wrong at least twice." For his many rural followers, being a Ragdyan means being open to expanding their horizons when the chance arrives, even if they're unable to go out and adventure themselves. The church of the mountain sage can be found in a plethora of places, from grandstanding, intricate temples to small shrines in remote villages, to the corners of restaurants in big cities and to prominently placed altars in taverns, where people from all over can come together and exchange tales of their lives. No matter the location, there will always be a depiction of Bahmenu with the Sage sitting atop it, hoping for the faithful to bless the shrines with the sound of laughter. Groups of traveling Ragdyan devotees go from inn to inn and put on shows filled with humorous anecdotes and the most ridiculous experiences the cast has ever had, working with the audience to bring forth riches of both coin and joy.

**Title** The Sage on the Mountain

**Areas of Concern** Humor, lessons, monkeys

**Edicts** Create humor in life, seek enlightenment through worldly experience, use harmless pranks to teach others

**Anathema** Discriminate based on social status, make a joke out someone's suffering, take control of another's life and agency

**Religious Symbol** bahmenu mountain

**Sacred Animal** monkey

**Sacred Colors** blue, red

**Source:** `= this.source` (`= this.source-type`)
