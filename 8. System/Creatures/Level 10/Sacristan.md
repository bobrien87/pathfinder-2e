---
type: creature
group: ["Fiend", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sacristan"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Greater Darkvision]]"
languages: "Common, Diabolic, Shadowtongue"
skills:
  - name: Skills
    desc: "Acrobatics +19, Athletics +22, Intimidation +18, Stealth +21, Torture Lore +16"
abilityMods: ["+6", "+5", "+6", "+0", "+3", "+2"]
abilities_top:
  - name: "Painsight"
    desc: "A velstrac automatically knows whether a creature it sees has any of the [[Doomed]], [[Dying]], and [[Wounded]] conditions as well as the value of those conditions."
armorclass:
  - name: AC
    desc: "30; **Fort** +22, **Ref** +19, **Will** +17"
health:
  - name: HP
    desc: "175; **Immunities** cold; **Weaknesses** silver 10, holy 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 10 (Deactivated by Holy or Silver)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Staggering Servitude"
    desc: "30 feet. When a creature ends its turn in the aura, it sees a vision of the sacristan groveling in pitiable servitude. The creature must succeed at a DC 27 [[Will]] save or become [[Stunned]] 1."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Barbed Chain +22 (`pf2:1`) (magical, reach 10 ft., trip, unholy, versatile s), **Damage** 1d6 spirit plus 2d6 bleed plus 2d8+9 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21<br>**3rd** [[Chilling Darkness]]<br>**1st** [[Fear]]"
abilities_bot:
  - name: "Focus Gaze"
    desc: "`pf2:1` The sacristan eerily stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against staggering servitude. In addition, if the creature was already stunned, on a failed save, its revulsion toward the sacristan's presence causes it to be [[Stupefied 2]] for 1 minute. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the sacristan's next turn."
  - name: "Shadow Scream"
    desc: "`pf2:3` **Frequency** once per hour <br>  <br> **Effect** The sacristan opens their mouth to unloose the wailing howls and mind-twisting darkness of the Netherworld. This creates a @Template[type:emanation|distance:30] of darkness and wailing sounds around the sacristan. Creatures with darkvision can't see through this darkness. The sacristan can Sustain Shadow Scream for up to 1 minute. Non-velstrac creatures in the area when the ability is used, as well as those who enter or start their turn in the area, must attempt a DC 28 [[Will]] save. <br> - **Critical Success** The creature is unaffected and is then temporarily immune for 24 hours. <br> - **Success** The creature is [[Deafened]] for 1 round. <br> - **Failure** The creature is [[Confused]] and deafened for 1 round. <br> - **Critical Failure** The creature takes @Damage[20[mental]|options:area-damage] damage, and is confused and deafened for 1 round."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sacristans are failures among the velstracs, creatures whose bodies and minds have been utterly broken by the velstracs' torments. These unfortunates are assembled from scrap metal, nerveless flesh, and bits of darkness into loyal agents who take ecstatic pleasure in serving other velstracs. Sacristans are empowered by a miniature gateway to the Netherworld deep in their mouths. By distending their jaws, they can howl with the shrieks and windstorms of that plane. Sacristans vary in appearance but are the size of average, if maimed, humans. Their features are redundant or absent, and barbed and rusted chains wrap around them.

The shadow-dwelling fiends known as velstracs all share a horrifying preoccupation with the search for ultimate sensation through self-mutilation. Velstracs transcend their stoic detachment only when inflicting pain and terror upon their victims, practicing new forms of torture, or turning their agonizing practices back on themselves. They consider themselves enlightened beings, transcending such limitations as morality or mortal taboos, but their victims know them as emotionless tormentors who inflict sadistic suffering. These fiends claim to seek perfection in thought, form, and action, although they don't recognize any refinement that doesn't require the painful excision of the flesh or spirit.

Velstracs manifest from the souls of the most extreme masochistic or sadistic mortals who are judged and sent on to the Netherworld. They take on forms that suit their vile predilections, ranging from the low-ranking augurs to the maestros of suffering and mutilation, the eremites. The process of transformation warps the soul step by step, with other velstracs conveying their new members through untold chambers of pain among the dark reaches of the Netherworld.

```statblock
creature: "Sacristan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
