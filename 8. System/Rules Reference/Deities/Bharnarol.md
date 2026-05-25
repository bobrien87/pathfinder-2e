---
type: deity
source-type: "Remaster"
domains: "Change, Creation, Duty, Knowledge"
favored-weapon: "Sickle"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Temporary Tool]], Rank 4: [[Creation]], Rank 5: [[Dreaming Potential]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In Nirvana, in a workshop nestled into the foothills of the Dragonmane Mountains, the Tempered Inventor toils away at his forge, working to create tools to support the creativity of others. His appearance is of a humanoid man with muscular arms, silver skin, and the head of an elephant. Preferring the heat of his forge and fires that inspire his own creativity, Bharnarol doesn't leave his domain often. On the occasions when he does choose to depart, it is to foster the gifts o f creativity, invention, and innovation in those who send him their prayers. Crafters who are blessed enough to encounter him are often those that need assurance that their creations are supporting positive growth in the world, versus those who venerate oppression or destruction.

Sadly, there are times that even his guidance is not enough to change the path of the inventor's intentions. In these times when he is unable to influence change, he will instead remove it from the possession of the inventor and lock it away in the Unflawed Vault, as even the most destructive of inventions he cannot bring himself to destroy. Within the walls of this vault exist some of the most threatening devices never known to mortals. This secure storage is located beneath his beloved forge, and only he holds the key to its entrance. While the inventions in the vault injure him in their negativity, he also knows that even evil inventions sometimes further the creativity of others.

**Title** The Tempered Inventor

**Areas of Concern** Creativity, invention, persistence

**Edicts** Follow creative sparks to the finish, create new and innovative things in your chosen medium, respect and admire the creativity of others

**Anathema** Destroy something created by hand without evil intent, discourage the innovation and creativity of others, abandon projects you have started rather than find ways to change them

**Religious Symbol** two mixing potions

**Sacred Animal** elephant

**Sacred Colors** blue, red

**Source:** `= this.source` (`= this.source-type`)
