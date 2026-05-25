---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gluttonyspawn"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +8, Stealth +9, Survival +10"
abilityMods: ["+4", "+3", "+4", "+0", "+2", "+1"]
abilities_top:
  - name: "Sin Scent (Imprecise) 30 feet"
    desc: "A sinspawn can smell creatures that reflect its sin as the scent ability. The GM determines which creatures are appropriately sinful. <br>  <br> Scent involves sensing creatures or objects by smell, and is usually a vague sense. The range is listed in the ability, and it functions only if the creature or object being detected emits an aroma (for instance, incorporeal creatures usually do not exude an aroma). <br>  <br> If a creature emits a heavy aroma or is upwind, the GM can double or even triple the range of scent abilities used to detect that creature, and the GM can reduce the range if a creature is downwind."
  - name: "Sinful Bite"
    desc: "A creature hit by the jaws of a sinspawn must attempt a DC 18 [[Will]] save as it is assailed by sinful thoughts. <br> - **Critical Success** Unaffected <br> - **Success** [[Sickened]] 1 <br> - **Failure** [[Sickened]] 2 <br> - **Critical Failure** sickened 2 plus [[Drained]] 1 for 1 minute"
armorclass:
  - name: AC
    desc: "16; **Fort** +10, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "30; **Immunities** controlled; **Resistances** mental 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "+4 Status to All Saves vs. Mental"
    desc: ""
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (agile, unarmed), **Damage** 1d8+4 piercing plus [[Sinful Bite]]"
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`) (unarmed), **Damage** 1d6+4 slashing"
  - name: "Melee strike"
    desc: "Scythe +10 (`pf2:1`) (deadly d10, trip), **Damage** 1d10+4 slashing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Sinspawn were created by one of seven ancient wizards known collectively as runelords—each of whom embraced and embodied one of seven sins. The first sinspawn was created by the Runelord of Wrath, utilizing techniques that have since gone on to influence fleshwarping practices. It wasn't long before the technique used to create sinspawn fell into the hands of the other runelords, and while each tried their own hand at crafting variants of their own design, today, sinspawn of wrath remain the most numerous and notorious of their kind.

Bearing only a vague resemblance to the humanoids from whose flesh they were formed, sinspawn generally appear horrifically emaciated and have unnaturally long arms and digitigrade legs, each with a trio of stubby, taloned digits. Veins bulge across sinspawn's bodies in sanguine patterns that suspiciously resemble twisted runes, and their flesh is pale and hairless. Their heads are elongated, with slits for a nose, red eyes, and disturbing lower jaws that split in half at the chin, revealing pedipalps that end in tiny, three-fingered hands and framing a long, lolling tongue.

Sinspawn stand 6-1/2 feet tall and typically weigh as much as an emaciated human of their size. They behave in a manner consistent with their associated sin and have physical characteristics that hint at these qualities. For example, greedspawn's veins appear to run with gold, while envyspawn appear even more gaunt than the rest of their kin.

```statblock
creature: "Gluttonyspawn"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
