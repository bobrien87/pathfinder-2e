---
type: deity
source-type: "Remaster"
domains: "Knowledge, Might, Travel, Vigil"
favored-weapon: "Light-pick"
divine-font: "Harm, Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Tailwind]], Rank 2: [[Knock]], Rank 5: [[Magic Passage]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Most dwarves consider the dour goddess Dranngvit to be a necessary evil, a harsh and acrimonious deity to whom one turns only when all other options have been exhausted. Dwarven legend holds that she was once betrothed to Torag and destined to become queen of the dwarven pantheon, only to be denied her promised throne when Torag fell in love with and chose Folgrit as his bride instead. Humiliated and embittered, Dranngvit withdrew from Forgeheart, the Heavenly domain of the dwarven gods, to dwell forever in self-imposed exile far from the rest of her pantheon with her great hound Hefnd as her sole companion.

The teachings of Dranngvit refer to debt in a myriad of forms, ranging from simply owing money or goods to the civil obligations that come with one's profession or position in society. Good or evil, legal or criminal, the precise nature of the debts are unimportant; according to Dranngvit's doctrines, all that matters is that every effort be made to repay them, in full and as expediently as possible. Nor does Dranngvit exclusively place the burden of this expectation upon the debtor. Crucially, Dranngvit's wrath is as likely to fall upon a predatory lender who knowingly ensnares others in debts they can never hope to settle as it is upon those who willfully attempt to avoid paying others what they owe.

**Title** The Debt Minder

**Areas of Concern** Debt, pursuit, vengeance

**Edicts** Help reclaim just debts, seek appropriate vengeance against transgressions

**Anathema** Allow a slight to go unrecognized, avoid repaying a debt, force others into debts you know are unpayable

**Religious Symbol** crossed picks

**Sacred Animal** hound

**Sacred Colors** gold, red

**Source:** `= this.source` (`= this.source-type`)
