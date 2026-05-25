---
type: deity
source-type: "Remaster"
domains: "Ambition, Confidence, Passion, Zeal"
favored-weapon: "Dueling-pistol"
divine-font: "Harm"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Charm]], Rank 4: [[Honeyed Words]], Rank 5: [[Cloak Of Colors]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

From a bacchanal gallery of gloried names remembered fondly, Ussharassim bids all who crave the warm embrace of fame, heroism, and renown to join the revelry. His kind are the young farmers who look over the glade dreaming of bards telling how they vanquished a great foe, the fiddlers who pray someone will play their song in a hundred years' time, the adventurer who wished everyone knew their name and smiled. Hopes for grand adventure are met with the demise of their loved ones, spurning on their campaign of revenge. Poets are gifted heartbreaks that rattle their core and inspire refrains that will be quoted for generations, the glory and honor of which are indebted to the Spurring Scar forever. From his table, surrounded by heroes, villains, and masters of their time, he shares tales of all who would be the next greats, his voice crystal clear from behind a mirror mask covering a scarred visage.

**Title** The Spurring Scar

**Areas of Concern** Fame, glory, legacy

**Edicts** Patron chroniclers and playwrights, perform dramatic entrances and exits, squeeze your connections for all they're worth, get the last word

**Anathema** Act with modesty or anonymity, perform great deeds without witnesses, let a slight go unrequited

**Religious Symbol** mirrored mask

**Sacred Animal** lap dog

**Sacred Colors** golden yellow

**Source:** `= this.source` (`= this.source-type`)
