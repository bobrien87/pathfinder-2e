---
type: creature
group: ["Aberration", "Amphibious"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nymolus"
level: "10"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: "Amphibious"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Aklo, Alghollthu, Common, Sakvroth, Thalassic (Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +22, Deception +22, Diplomacy +18, Intimidation +18, Occultism +21, Society +19, Stealth +18, Lore (any five subcategories) +21"
abilityMods: ["+5", "+2", "+4", "+6", "+4", "+6"]
abilities_top:
  - name: "Inhabit Ugothol"
    desc: "The nymolus spends 10 minutes with a willing ugothol to become enmeshed with the creature. The nymolus then fully inhabits the ugothol's body. While inhabited, the ugothol retains its mental abilities, but its body is completely controlled by the nymolus. The nymolus and ugothol each have an initiative count as if they were separate creatures. The nymolus can't use any ability that relies on their physical form while inhabiting the ugothol, but the nymolus can still perceive and cast spells normally. The two remain enmeshed until the nymolus uses the ugothol's Assume Form ability to separate them, or until the ugothol is slain. If the ugothol dies, the nymolus becomes [[Stunned]] 3 due to the force of the separation."
  - name: "Replace Recollection"
    desc: "The nymolus can spend 10 minutes to replace any memory with another memory they have access to via a memory crystal."
armorclass:
  - name: AC
    desc: "28; **Fort** +20, **Ref** +15, **Will** +22"
health:
  - name: HP
    desc: "190"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +23 (`pf2:1`) (agile, reach 15 ft., versatile p), **Damage** 2d10+10 bludgeoning plus [[Grab]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30, attack +21<br>**5th** [[Mind Probe]]<br>**4th** [[Mirage]], [[Rewrite Memory]]<br>**3rd** [[Mind Reading]] (At Will), [[Paralyze]]<br>**1st** [[Daze]], [[Electric Arc]], [[Guidance]], [[Mindlink]] (At Will), [[Soothe]]"
abilities_bot:
  - name: "Extract Memory"
    desc: "`pf2:3` **Requirements** The target creature must be [[Grabbed]], [[Paralyzed]], [[Restrained]], [[Unconscious]], or willing; Efect The nymolus reaches into an adjacent creature's memory and extracts up to 10 minutes of the target's experiences, forming them into a memory crystal within the nymolus's brain. The target creature must attempt a DC 27 [[Will]] save to avoid losing its memory. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature loses the target memory. <br> - **Failure** The creature loses the target memory and is [[Confused]] for 1 minute. <br> - **Critical Failure** As failure, but the creature can only roll to end this condition if it takes damage from the nymolus themself or if counteracted by an efect of at least 13th level or 7th rank."
  - name: "Stunning Pulse"
    desc: "`pf2:2` The nymolus emits a powerful mental pulse that overwhelms nearby creatures. Creatures in a @Template[type:emanation|distance:10] must attempt a DC 27 [[Fortitude]] save to avoid being stunned. The nymolus can't use Stunning Pulse again for 1d4 rounds. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Stunned]] 1. <br> - **Failure** The creature is [[Stunned]] 2. <br> - **Critical Failure** The creature is [[Stunned]] 3."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Alghollthus share a genetic memory and are theoretically capable of recalling every experience dating back to the existence of the frst alghollthu hundreds of millions of years ago.

Accessing these memories all at once would be lethally taxing to most alghollthus, but nymoluses are different. They revel in tapping into this genetic memory and add to it by stealing memories from others, turning them into memory crystals. A single nymolus can store up to 10 crystals at a time within their brain, replacing more mundane ones as they fll this storage and keeping the rest in collections among their lairs. To collect memories, nymoluses venture further from the seas than some of their siblings by establishing symbiotic links with ugothols. They're able to coordinate with these creatures by reshaping their bodies, then compressing and interweaving their fesh into the ugothols, which allows them to search for rare and intriguing recollections.

```statblock
creature: "Nymolus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
