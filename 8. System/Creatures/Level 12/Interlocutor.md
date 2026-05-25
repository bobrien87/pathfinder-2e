---
type: creature
group: ["Fiend", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Interlocutor"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Greater Darkvision]]"
languages: "Common, Diabolic, Shadowtongue"
skills:
  - name: Skills
    desc: "Athletics +25, Crafting +22, Intimidation +25, Medicine +26, Religion +22, Stealth +19, Torture Lore +20"
abilityMods: ["+7", "+3", "+5", "+2", "+6", "+5"]
abilities_top:
  - name: "Painsight"
    desc: "A velstrac automatically knows whether a creature it sees has any of the [[Doomed]], [[Dying]], and [[Wounded]] conditions as well as the value of those conditions."
armorclass:
  - name: AC
    desc: "33; **Fort** +23, **Ref** +21, **Will** +26"
health:
  - name: HP
    desc: "215; **Immunities** cold; **Weaknesses** holy 15, silver 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 20 (Deactivated by Holy or Silver)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Glimpse of Stolen Flesh"
    desc: "30 feet. When a creature ends its turn in the aura, it sees pieces of its own body amid the interlocutor's form. The creature must succeed at a DC 29 [[Will]] save or become [[Stunned]] 1."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shadow Siphon"
    desc: "`pf2:r` **Trigger** The interlocutor would take damage from a spell or magical effect <br>  <br> **Effect** The interlocutor takes half the triggering damage instead."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +25 (`pf2:1`) (deadly 2d10, magical, reach 10 ft., unholy), **Damage** 3d10+13 bludgeoning plus 2d6 bleed"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 33, attack +25<br>**7th** [[Interplanar Teleport (self only, to the Netherworld or the Universe only)]]<br>**5th** [[Breath of Life]]<br>**2nd** [[Sound Body]]<br>**1st** [[Heal]], [[Stabilize]]"
abilities_bot:
  - name: "Focus Gaze"
    desc: "`pf2:1` The interlocutor stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against glimpse of stolen flesh. In addition, if the creature was already stunned, on a failed save, it feels its internal organs twist and writhe, and is [[Clumsy]] 2 for 1 minute. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the interlocutor's next turn."
  - name: "Surgical Rend"
    desc: "`pf2:1` This functions as the [[Rend]] ability, dealing claw Strike damage. In addition, if the target is a living creature with organs and muscle, the interlocutor opens a precise wound. Until the creature is restored to its maximum Hit Points, thus closing the wound, Strikes against the creature deal an additional 1d6 precision damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Interlocutors are the most talented surgeon-sculptors of the velstracs, carving away flesh and replacing it with new body parts of muscle, sinew, and metal. Each interlocutor structures their individual appearance carefully, but all are towering, multi-limbed amalgamations of the strongest limbs, densest bones, and sharpest metals they can find. They continually search for new material to graft to their forms, and their slain foes are rarely found intact, as little is more valuable to interlocutors than a powerful opponent's legs, eyes, or even brain. Due to their unique properties, deposits of skymetals sometimes draw interlocutors to the mortal Universe. Interlocutors average 9 feet in height and weigh approximately 800 pounds.

The shadow-dwelling fiends known as velstracs all share a horrifying preoccupation with the search for ultimate sensation through self-mutilation. Velstracs transcend their stoic detachment only when inflicting pain and terror upon their victims, practicing new forms of torture, or turning their agonizing practices back on themselves. They consider themselves enlightened beings, transcending such limitations as morality or mortal taboos, but their victims know them as emotionless tormentors who inflict sadistic suffering. These fiends claim to seek perfection in thought, form, and action, although they don't recognize any refinement that doesn't require the painful excision of the flesh or spirit.

Velstracs manifest from the souls of the most extreme masochistic or sadistic mortals who are judged and sent on to the Netherworld. They take on forms that suit their vile predilections, ranging from the low-ranking augurs to the maestros of suffering and mutilation, the eremites. The process of transformation warps the soul step by step, with other velstracs conveying their new members through untold chambers of pain among the dark reaches of the Netherworld.

```statblock
creature: "Interlocutor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
