---
type: creature
group: ["Aberration", "Tanggal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Penanggalan"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: "Tanggal"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Aklo, Common"
skills:
  - name: Skills
    desc: "Athletics +12, Deception +14, Intimidation +12, Stealth +14, Midwifery Lore +9"
abilityMods: ["+3", "+5", "+2", "+0", "+2", "+5"]
abilities_top:
  - name: "Penanggalan Bile"
    desc: "Rest doesn't decrease the drained value from penanggalan bile <br>  <br> **Saving Throw** DC 19 [[Fortitude]] save <br>  <br> **Stage 1** [[Drained]] 1 (1 week) <br>  <br> **Stage 2** [[Drained]] 2 (1 week) <br>  <br> **Stage 3** [[Drained]] 3 (1 week) <br>  <br> **Stage 4** dead"
armorclass:
  - name: AC
    desc: "22; **Fort** +9, **Ref** +16, **Will** +11"
health:
  - name: HP
    desc: "85; **Weaknesses** slashing 5"
abilities_mid:
  - name: "Spewing Bile"
    desc: "When the penanggalan takes slashing damage, their wound spews bile on adjacent creatures, dealing 2d10 poison damage (DC 19 [[Fortitude]] save). <br>  <br> The penanggalan loses their spewing bile and penanggalan bile abilities until the end of their next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Proboscis Tongue +15 (`pf2:1`) (finesse), **Damage** 2d6+5 piercing plus [[Penanggalan Bile]]"
  - name: "Melee strike"
    desc: "Entrails +13 (`pf2:1`), **Damage** 2d4+5 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d4+3)[bludgeoning]], DC 21 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Elongate Tongue"
    desc: "`pf2:1` The penanggalan's tongue extends, the membrane stretching and becoming translucent. Until the end of the turn, the penanggalan's proboscis tongue Strikes have a 10-foot reach, and any target is [[Off Guard]] against the Strike unless it has a Perception DC of 22 or higher or the ability to precisely sense [[Invisible]] things."
  - name: "Ride Corpse"
    desc: "`pf2:3` The penanggalan inserts their entrails into their humanoid body, allowing them to appear as and move about like a normal human. The body has 10 Hit Points and the same defenses as the penanggalan. <br>  <br> When the body is destroyed, the penanggalan is ejected unharmed. The body becomes a corpse, and if it is neither controlled by the penanggalan nor stored in an alchemical vat, it decays as normal."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Penanggalans feed on the blood and entrails of the young. When their cannibalistic hunger strikes, penanggalans bathe their bodies in an alchemical substance that smells like vinegar. Once submerged in the concoction, their neck rips from side to side, allowing their head to float upward and pull out their lungs, stomach, and intestines. They leave their bodies in the vinegar bath much like a molting crab leaves its old shell, then fly off to find a victim filled with blood and guts.

As grotesque as these creatures are when hungry, the penanggalan appears young and healthy while wearing their body. Such is the nature of their existence: they consorted with otherworldy beings, gaining a lifetime of youth in exchange for an evil hunger for the young. But they are not immortal. They age and die normally like the people they once were-they just retain their youthfulness throughout this existence.

It can be difficult to spot a penanggalan among the populace. The faint scar ringing their neck at the point of separation can be explained away as a blemish, and it can be hidden under a flashy necklace. Meanwhile the faint, sour scent of a penanggalan's preserved body, while peculiar, is not uncommon in the sweaty tropics they frequent.

```statblock
creature: "Penanggalan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
