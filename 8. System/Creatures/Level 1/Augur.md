---
type: creature
group: ["Fiend", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Augur"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Greater Darkvision]]"
languages: "Common, Diabolic, Shadowtongue (can't speak any language)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Deception +6, Intimidation +7, Religion +4, Stealth +8, Torture Lore +7"
abilityMods: ["-1", "+3", "+1", "+2", "+1", "-1"]
abilities_top:
  - name: "Painsight"
    desc: "A velstrac automatically knows whether a creature it sees has any of the [[Doomed]], [[Dying]], and [[Wounded]] conditions as well as the value of those conditions."
armorclass:
  - name: AC
    desc: "17; **Fort** +4, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "15; **Immunities** cold; **Weaknesses** holy 5, silver 5"
abilities_mid:
  - name: "Regeneration 2 (Deactivated by Holy or Silver)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Feel the Blades"
    desc: "30 feet. When a creature ends its turn in the aura, it feels the sharp barbs of the augur's blades on its skin. The creature must succeed at a DC 17 [[Will]] save or become [[Frightened]] 1 ([[Frightened]] 2 on a critical failure)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Blade +8 (`pf2:1`) (agile, finesse, magical, unholy, versatile p), **Damage** 1d4 bleed plus 1d4-1 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**4th** [[Read Omens (once per week)]]<br>**2nd** [[Augury]]<br>**1st** [[Harm]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Focus Gaze"
    desc: "`pf2:1` The augur stares at a creature they can see within 30 feet. The target must immediately attempt a Will save against feel the blades. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the augur's next turn."
  - name: "Whilring Slice"
    desc: "`pf2:2` The augur Flies or Strides, whirling as they move. The augur deals the damage of their blade Strike to each creature whose space they enter (DC 16 [[Reflex]] save). Each creature is affected only once, even if the augur moves through its space multiple times."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These spherical knots of sinewy muscle, serrated blades, and bloody metal are the most common velstracs on the Netherworld. Each augur has only a single eye, from which they can witness the horrors inflicted by other velstracs, who train the augur to expect and appreciate pain. Augurs are 1 foot in diameter and weigh 30 pounds.

The shadow-dwelling fiends known as velstracs all share a horrifying preoccupation with the search for ultimate sensation through self-mutilation. Velstracs transcend their stoic detachment only when inflicting pain and terror upon their victims, practicing new forms of torture, or turning their agonizing practices back on themselves. They consider themselves enlightened beings, transcending such limitations as morality or mortal taboos, but their victims know them as emotionless tormentors who inflict sadistic suffering. These fiends claim to seek perfection in thought, form, and action, although they don't recognize any refinement that doesn't require the painful excision of the flesh or spirit. Velstracs manifest from the souls of the most extreme masochistic or sadistic mortals who are judged and sent on to the Netherworld. They take on forms that suit their vile predilections, ranging from the low-ranking augurs to the maestros of suffering and mutilation, the eremites. The process of transformation warps the soul step by step, with other velstracs conveying their new members through untold chambers of pain among the dark reaches of the Netherworld.

```statblock
creature: "Augur"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
