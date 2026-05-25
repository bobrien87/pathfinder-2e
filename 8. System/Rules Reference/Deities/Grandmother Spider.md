---
type: deity
source-type: "Remaster"
domains: "Creation, Family, Fate, Trickery"
favored-weapon: "Bola"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Pest Form]], Rank 2: [[Web]], Rank 4: [[Honeyed Words]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Also known as Nana Anadi, Grandmother Spider began her existence as a servant of the other gods, meant to weave fate and reality into existence. Infuriated at her position as a lackey, she made fools of the greater gods through mischief and disruption. She stole and copied Asmodeus' keys, resulting in widespread chaos, and pilfered some of Sarenrae's fire, leading numerous followers astray. Nimbly avoiding any retribution for her antics, Grandmother Spider rewove the strands of fate for herself, gaining her freedom. She regularly pleads with her brother Achaekek to follow her lead and rebel against the gods, and while he always refuses, seemingly indifferent, Achaekek has on one notable occasion proven vengeful toward those who harm his sister or her followers.

**Title** The Weaver

**Areas of Concern** family, illusion, stories, twilight, weaving

**Edicts** be skilled and clever, think for yourself, take due payment for your work, humiliate the powerful

**Anathema** abuse someone you have power over, harm someone who has given you sincere kindness, let a slight go unanswered, own a slave

**Religious Symbol** four-pointed hollow webbed diamond

**Sacred Animal** spider

**Sacred Colors** blue, orange, yellow

**Source:** `= this.source` (`= this.source-type`)
