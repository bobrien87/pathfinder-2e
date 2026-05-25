---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "wornring"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Sealed inside the hidden compartment of a gold ring, *heartblood* has an unmistakable coppery taste, along with a thick mouth feel. A whiff of the concoction is pleasantly stimulating.

**Stage 1 (1 Week)** The first time you enter this stage from a particular dose of *heartblood*, you are affected as if by regenerate. Each round this effect functions, it attempts to counteract one disease or poison affecting you with a bonus equal to your class DC – 10. *Heartblood* also reduces physical signs of aging, altering your appearance to that of vigorous adulthood for your ancestry. (Non-adults who drink *heartblood* change only in apparent vigor, not age.)

You have fast healing equal to half your level, as well as resistance to void damage and poison damage equal to half your level. Also, you gain a +1 circumstance bonus to saving throws (or any other defense) against death effects, disease, paralysis, poison, and sleep. Treat the outcome of any saving throw you roll against death, paralyze, or sleep effects as one step better.

**Stage 2 (1 Month)** You gain low-light vision, or you gain darkvision if your ancestry already has low-light vision. Reduce your current and maximum Hit Points by 2 × your level; you are [[Doomed]] 1. You develop a pallor and a dislike of bright light, especially sunlight. If suddenly exposed to bright light, you are [[Dazzled]] until the end of your next turn. While in an area of sunlight, you remain dazzled until 1 round after the exposure ends. Normal food is unsatisfying, and you have urges to consume blood; when confronted with the opportunity to do so, you must succeed at a Will save to avoid it. Doing so once after each time you roll initiative is enough. Your normal coloration returns for a few hours after you drink blood.

If you die at this stage or higher, your body becomes a bloody mist that sinks 6 feet into the ground. The third night thereafter, you rise from the earth as a vampire. This typically makes you unholy. You are under the control of the *heartblood*'s creator unless your level is higher than that creature's. The controlling vampire senses you and guides you to them via psychic link. Significant destruction of your body and circumstances that prevent the formation of undead stop this effect.

**Stage 3 (1 Month)** You gain darkvision and now have fast healing equal to your level. A death effect can't automatically kill you or increase your dying value. Reduce your current and maximum Hit Points by 4 × your level, rounded up, instead of 2 × your level; you are [[Doomed]] 2. Your hunger for blood increases, so if you fail to drink a cup or so each day, you are considered to have gone without food that day. You are also [[Slowed]] 1 while in sunlight, becoming [[Slowed]] 2 after 1 minute. Your shadow is wispy, and your reflection in mirrors ghostly, which are apparent signs of vampirism to those who know such facts.

**Stage 4** You die.

**Purging** *Heartblood* loses its potency if the vampire who created it is destroyed. However, a dose of *heartblood* imposes a –2 status penalty to your saving throws against the powers of the vampire who created it.

**Source:** `= this.source` (`= this.source-type`)
