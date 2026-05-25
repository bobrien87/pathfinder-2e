---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Cursed]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This jagged shard of bone appears to be and functions as a *+1 striking dagger* with a sharp edge that is perpetually stained with blood. Whenever you critically hit with the weapon, you deal an additional 1d6 persistent bleed damage, but you also take 1d6 persistent,bleed damage. You take a –2 penalty to the flat check to remove this bleed damage, and when you succeed at this flat check, you are exposed to Verex's ruin (see below) as the site of the injury grows red and inflamed, your blood vessels discoloring and swelling as if serrated knives were trying to push their way out.

Once the curse has activated for the first time, the weapon fuses to you; while you can sheathe the dagger outside of combat, it appears in your hand when a fight begins and you can't sheathe it as long as there is an enemy you can perceive.

**Verex's Ruin** (disease, unholy)

**Saving Throw** DC 22 [[Fortitude]] save

**Onset** 1 hour

**Stage 1** [[Enfeebled]] 1 (1 day)

**Stage 2** [[Enfeebled]] 2, [[Fatigued]], and 1d6 spirit damage each time you would take persistent bleed damage (1 week)

**Stage 3** as stage 2, but the spirit damage increases to 2d6 (1 week)

**Stage 4** [[Enfeebled]] 3, fatigued, and 4d6 spirit damage each time you would take persistent bleed damage (1 week)

**Stage 5** death

**Source:** `= this.source` (`= this.source-type`)
