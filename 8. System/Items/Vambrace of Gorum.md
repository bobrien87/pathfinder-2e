---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Artifact]]", "[[Divine]]", "[[Magical]]"]
price: "{'cp': 0, 'pp': 0, 'sp': 0}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When the Lord in Iron shattered, immeasurable fragments fell to Golarion as pieces of metal. This piece of his armor has been shaped into the Vambrace of Gorum, a supreme reinforcing high-grade adamantine shield (Hardness 20, HP 160, BT 80). Pieces of sharp iron stick out, acting as +3 major striking shield spikes. The Vambrace still holds some of the deity's power. When the shield is broken, small fragments of metal explode outward, dealing @Damage[6d6[piercing]|options:area-damage] damage in a @Template[type:cone|distance:15] (DC 40 [[Reflex]] save).

**Activate—Blade of Iron** `pf2:2` (concentrate, divine, manipulate)

**Frequency** once per day

**Effect** The shield reforms into a +3 high-grade adamantine major striking greatsword for 1 minute. While wielding this sword, you gain a +1 circumstance bonus to AC for each adjacent enemy (up to a +4 bonus).

**Activate—Blood of Iron** `pf2:1` (aura, divine)

**Frequency** once per day

**Requirements** The Vambrace of Gorum is in its shield form

**Effect** Your shield becomes an empowering symbol of the thrill of battle. You and your allies within 10 feet of you gain 30 temporary Hit Points that last for 1 hour, and reduce your clumsy, enfeebled, frightened, and stupefied conditions by 1.

**Activate—Bones of Iron** `pf2:r`

**Frequency** once per 10 minutes

**Trigger** You use the shield to Shield Block and the attack overcomes the shield's Hardness

**Effect** The iron spikes lash out at the creature who made the attack. The creature takes @Damage[6d6[piercing],3d6[persistent,bleed]|options:area-damage]{6d6 piercing damage and 3d6 persistent bleed damage} (DC 40 [[Reflex]] save).

**Destruction** If the Vambrace of Gorum is broken, buried under a rose bush in Nirvana, and left undisturbed for 100 years, it loses all its magic and becomes a standard steel shield.

**Source:** `= this.source` (`= this.source-type`)
