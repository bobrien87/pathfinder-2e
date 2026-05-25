---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Seraptis"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Chthonian, Draconic, Empyrean (Telepathy 100 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +30, Athletics +31, Deception +29, Religion +27, Stealth +28"
abilityMods: ["+8", "+7", "+6", "+3", "+4", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "37; **Fort** +27, **Ref** +28, **Will** +25"
health:
  - name: HP
    desc: "340; blood healing; **Weaknesses** cold iron 15, holy 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Blood Healing"
    desc: "30 feet. <br>  <br> Whenever a humanoid within the aura takes bleed damage, the blood flows through the air to the seraptis's mouths and the seraptis heals by the same amount."
  - name: "Recovery Vulnerability"
    desc: "When a creature within the seraptis's blood healing aura recovers from persistent damage, the seraptis takes 3d6 mental damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Wounding Scimitar +32 (`pf2:1`) (forceful, magical, sweep, unholy), **Damage** 1d6 bleed plus 2d6+16 slashing plus 2d6 mental"
  - name: "Melee strike"
    desc: "Claw +31 (`pf2:1`) (agile, magical, unarmed, unholy), **Damage** 2d4+16 slashing plus 2d6 mental plus [[Grab]]"
  - name: "Melee strike"
    desc: "Caustic Blood +30 (`pf2:1`) (acid, magical, unholy), **Damage** 7d6 acid"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 35, attack +27<br>**6th** [[Dominate]], [[Phantasmal Calamity]], [[Truesight]] (Constant)<br>**5th** [[Truespeech]] (Constant), [[Wave of Despair]]<br>**4th** [[Translocate]], [[Translocate]] (At Will)<br>**1st** [[Illusory Disguise]] (At Will)"
abilities_bot:
  - name: "Bloody Dance"
    desc: "`pf2:2` The seraptis makes a Strike with up to four arms, each against a different target and using a claw or scimitar as appropriate. These attacks count toward the seraptis's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks. The seraptis can use Grab following this activity, separately attempting to [[Grapple]] each creature hit by a claw."
  - name: "Gnawing Arms"
    desc: "`pf2:1` **Requirements** The seraptis has at least one creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The seraptis's arm mouths gnaw on those creatures, dealing each of them @Damage[(2d6+8)[piercing]] damage with a DC 37 [[Fortitude]] save. Creatures that fail the save also take 2d6 persistent bleed damage."
  - name: "Isolating Words"
    desc: "`pf2:1` The seraptis telepathically explains a plausible secret to a creature within 30 feet. That creature must succeed at a DC 37 [[Will]] save or be mentally cut off from those around them for 1 minute (or permanently on a critical failure). The affected creature treats no one as an ally and any speech they hear is warped, encouraging conflict, and negating any linguistic ability from creatures that aren't unholy. <br>  <br> Regardless of the results of the saving throw, the creature is immune to Isolating Words for 24 hours."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Four-armed seraptis demons are radical nihilists at heart, despising other creatures out of bitter entitlement and laughing hysterically when others die or suffer. They arise from souls that engaged in dedicated campaigns of misery, driving their victims toward despair and suicide. After their awakening as a seraptis, the hungry mouths carved into their arms devour others' suffering, bringing a lively hue to the demon's cold skin.

These demons seek to drag mortals down to their level, luring pawns into deepseated resentment. Feeding their targets an unending stream of half-truths and propaganda, they often drive these mortals to vent their rage into unforgivable deeds against innocents. Although thrilled by the misery their mortal pawns inflict, the demons' true comfort is to harvest the souls of those pawns as more of their kind.

When a sinful mortal soul is judged and sent on to the Outer Rifts, it can become a deadly fiend—a demon. Demons are living incarnations of sin—be they classic sins like wrath or gluttony, or more "specialized" depravities like an obsession with torture or the act of treason or treachery. Once formed, a demon's driving goals are twofold—the amassing of personal power, and the corruption of mortal souls to cause them to become tainted by sin. In this way demons ensure a never-ending supply of new demons to bolster their ever-growing ranks in the Outer Rifts.

Demons are selfish and self-absorbed creatures, and most firmly believe that mortals only play at being more virtuous than fiends. They enjoy tempting mortals into damnation to both indulge their egos and swell their armies. Like many other fiends, one of the great rewards of this manipulation is fulfilling their hunger for souls. In their eyes, the primary use for these souls is to spawn new demons, who can serve as soldiers, slaves, pawns, or even currency for their more powerful masters.

```statblock
creature: "Seraptis"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
